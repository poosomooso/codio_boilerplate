
import os, json, uuid

num_mcq = 15
num_frq = 2

assessment_path = os.path.join(".guides", "assessments")
content_path = os.path.join(".guides", "content")

def init():
    try: 
        os.mkdir(os.path.join(".guides", "secure"))
    except:
        pass
    try: 
        os.mkdir(os.path.join(".guides", "secure", "key"))
    except:
        pass
    try: 
        os.mkdir(assessment_path)
    except:
        pass
    try: 
        os.mkdir(content_path)
    except:
        pass

def gen_mcq(question_num):
    id = uuid.uuid4()
    id = str(id)
    filestem = f'MCQ-{question_num:02d}'
    # content json
    content = f'''{{
	"id": "{id}",
	"title": "MCQ Question {question_num}",
	"files": [
		{{
			"path": "#tabs",
			"action": "close"
        }}
	],
	"path": [],
	"contentType": "markdown",
	"type": "page",
	"teacherOnly": false,
	"closeTerminalSession": true,
	"learningObjectives": "",
	"layout": "1-panel"
    }}'''
    cfname = os.path.join(content_path, filestem+".json")
    with open(cfname, "w") as f:
        f.write(content)

    mcq_filestem = f'multiple-choice-{id[0:8]}{question_num:02d}'
    # mcq json
    mcq_deets = f'''{{
	"type": "multiple-choice",
	"taskId": "{mcq_filestem}",
	"source": {{
		"name": "MCQ {question_num}",
		"showName": true,
		"instructions": "Question ????",
		"multipleResponse": false,
		"isRandomized": false,
		"answers": [
			{{
				"_id": "{str(uuid.uuid4())}",
				"correct": false,
				"answer": "A"
			}},
			{{
				"_id": "{str(uuid.uuid4())}",
				"correct": false,
				"answer": "B"
			}},
			{{
				"_id": "{str(uuid.uuid4())}",
				"correct": false,
				"answer": "C"
			}},
			{{
				"_id": "{str(uuid.uuid4())}",
				"correct": true,
				"answer": "D"
			}},
			{{
				"_id": "{str(uuid.uuid4())}",
				"correct": false,
				"answer": "E"
			}}
		],
		"metadata": {{
			"tags": [
				{{
					"name": "Assessment Type",
					"value": "Multiple Choice"
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
		"showExpectedAnswerOption": {{
			"type": "Never"
		}},
		"points": 20,
		"incorrectPoints": 0,
		"arePartialPointsAllowed": false,
		"useMaximumScore": false
	}}
}}'''
    mcqname = os.path.join(assessment_path, mcq_filestem+".json")
    with open(mcqname, "w") as f:
        f.write(mcq_deets)

    md_content = f'''{{Check It!|assessment}}({mcq_filestem})'''
    mdname = os.path.join(content_path, filestem+".md")
    with open(mdname, "w") as f:
        f.write(md_content)

    return filestem

def gen_frq(question_num):
    id = uuid.uuid4()
    id = str(id)
    filestem = f'FRQ-{question_num:02d}'
    # content json
    content = f'''{{
	"id": "{id}",
	"title": "Question {question_num}",
	"files": [
		{{
			"path": "#tabs",
			"action": "close"
		}},
		{{
			"path": "#preview: {filestem}.md",
			"panel": 0,
			"action": "open"
		}}
	],
	"path": [],
	"contentType": "markdown",
	"type": "page",
	"teacherOnly": false,
	"closeTerminalSession": true,
	"learningObjectives": "",
	"layout": "2-panels"
    }}'''
    cfname = os.path.join(content_path, filestem+".json")
    with open(cfname, "w") as f:
        f.write(content)

    frq_filestem = f'free-text-{id[0:8]}{question_num:02d}'
    # frq json
    frq_deets = f'''{{
	"type": "free-text",
	"taskId": "{frq_filestem}",
	"source": {{
		"name": "FRQ {question_num}",
		"showName": true,
		"instructions": "Thing",
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

    md_content = f'''{{Check It!|assessment}}({frq_filestem})'''
    mdname = os.path.join(content_path, filestem+".md")
    with open(mdname, "w") as f:
        f.write(md_content)
    with open(filestem+".md", "w") as f:
        pass # empty file

    return filestem


files_in_order = []

for i in range(num_mcq):
    filestem = gen_mcq(i)
    files_in_order.append(filestem)

for i in range(num_frq):
    filestem = gen_frq(i)
    files_in_order.append(filestem)

with open(os.path.join(content_path, "index.json"), "r+") as f:
        data = json.load(f)
        data["order"] = files_in_order
        f.seek(0)
        json.dump(data, f, indent=2)
