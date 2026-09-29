import os, json, uuid

assessment_path = os.path.join(".guides", "assessments")
content_path = os.path.join(".guides", "content")

# will append to all md files in guides

def gen_frq(page_name):
    id = uuid.uuid4()
    id = str(id)

    frq_filestem = f'free-text-{id[0:8]}'
    # frq json
    frq_deets = f'''{{
	"type": "free-text",
	"taskId": "{frq_filestem}",
	"source": {{
		"name": "Revision",
		"showName": true,
		"instructions": "* What is the correct answer?\\n* Why did you pick the answer you did?\\n* Why is the correct answer correct?",
		"metadata": {{
			"tags": [
				{{
					"name": "Assessment Type",
					"value": "Free Text"
				}}
			],
			"files": [],
			"opened": []
		}},
		"bloomsObjectiveLevel": "",
		"learningObjectives": "",
		"guidance": "",
		"showGuidanceAfterResponseOption": {{
			"type": "Never"
		}},
		"maxAttemptsCount": 0,
		"previewType": "NONE",
		"arePartialPointsAllowed": false,
		"points": 20,
		"rubrics": []
	}}
}}'''
    mcqname = os.path.join(assessment_path, frq_filestem+".json")
    with open(mcqname, "w") as f:
        f.write(frq_deets)

    md_content = f'''
{{Submit Answer|assessment}}({frq_filestem})'''
    mdname = os.path.join(content_path, page_name+".md")
    with open(mdname, "a") as f:
        f.write(md_content)




for e in os.scandir(content_path):
    if e.is_file() and e.name.endswith("md"):
        gen_frq(e.name[:-3]) # cut off .md