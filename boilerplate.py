# must be run from root directory

### params

title = "Table Reservations"
fname = "table"
testid = "test-2205381053"
guidePageFname = "Table-reservations-d2cd"
hasInput = True

import os, json


def init():
    try:
        os.mkdir("code")
    except:
        pass
	try: 
        os.mkdir(os.path.join(".guides", "secure"))
    except:
        pass
    try: 
        os.mkdir(os.path.join(".guides", "secure", "key"))
    except:
        pass

def exercise():
    """
    * set exercise params (json)
    * boilerplate helper
    * create key
    * create starter file
    * set layout
    * add buttons
    """
    terminal_code = """,
				{
					"type": "terminal",
					"panelNumber": 1,
					"content": ""
				}"""
    exercise_details = f"""{{
	"type": "test",
	"taskId": "{testid}",
	"source": {{
		"name": "{title}",
		"showName": true,
		"instructions": "",
		"command": "python3 .guides/secure/{fname}_helper.py",
		"timeoutSeconds": 40,
		"metadata": {{
			"tags": [
				{{
					"name": "Assessment Type",
					"value": "Advanced Code Test"
				}}
			],
			"files": [
				"code/{fname}.py"
			],
			"opened": [
				{{
					"type": "file",
					"panelNumber": 0,
					"content": "code/{fname}.py"
				}}{terminal_code if hasInput else ""}
			]
		}},
		"bloomsObjectiveLevel": "",
		"learningObjectives": "",
		"guidance": "",
		"showGuidanceAfterResponseOption": {{
			"type": "Never"
		}},
		"maxAttemptsCount": 3,
		"points": 20,
		"arePartialPointsAllowed": false,
		"useMaximumScore": false
	}}
}}
"""
    with open(os.path.join(".guides", "assessments", f"{testid}.json"), "w") as f:
        f.write(exercise_details)

    helper_code = f"""import os
import subprocess
import sys
from difflib import unified_diff


path = "code"
file = "{fname}.py"
student_code = os.path.join(path, file)


key_code = os.path.join(".guides", "secure", "key", "{fname}_key.py")


def print_input_check(label, input_txt, diff):
  print(label + " ---------------------")
  print("Inputs:")
  print(input_txt)
  print("Expected: '-'; Actual: '+'")
  print('\\n'.join(list(diff)))
  print()




def check_output(file):
  input_txt = b"19\\n"
  student_output = subprocess.check_output(["python3", file], input=input_txt, timeout=120).strip().decode("utf-8")
  actual_output = subprocess.check_output(["python3", key_code], input=input_txt, timeout=120).strip().decode("utf-8")
  diff = unified_diff(actual_output.splitlines(), student_output.splitlines(), lineterm='', n=10)
  print_input_check("Test 0", input_txt, diff)
  return student_output == actual_output


def test1(file):
  input_txt = b"16\\n"
  student_output = subprocess.check_output(["python3", file], input=input_txt, timeout=120).strip().decode("utf-8")
  actual_output = subprocess.check_output(["python3", key_code], input=input_txt, timeout=120).strip().decode("utf-8")
  diff = unified_diff(actual_output.splitlines(), student_output.splitlines(), lineterm='', n=10)
  print_input_check("Test 1", input_txt, diff)
  return student_output == actual_output


def test2(file):
  input_txt = b"18\\n"
  student_output = subprocess.check_output(["python3", file], input=input_txt, timeout=120).strip().decode("utf-8")
  actual_output = subprocess.check_output(["python3", key_code], input=input_txt, timeout=120).strip().decode("utf-8")
  diff = unified_diff(actual_output.splitlines(), student_output.splitlines(), lineterm='', n=10)
  print_input_check("Test 2", input_txt, diff)
  return student_output == actual_output

def test3(file):
  input_txt = b"27\\n"
  student_output = subprocess.check_output(["python3", file], input=input_txt, timeout=120).strip().decode("utf-8")
  actual_output = subprocess.check_output(["python3", key_code], input=input_txt, timeout=120).strip().decode("utf-8")
  print("Test 3:")
  print("(hidden)")
  print()
  return student_output == actual_output

def test4(file):
  input_txt = b"12\\n"
  student_output = subprocess.check_output(["python3", file], input=input_txt, timeout=120).strip().decode("utf-8")
  actual_output = subprocess.check_output(["python3", key_code], input=input_txt, timeout=120).strip().decode("utf-8")
  print("Test 4:")
  print("(hidden)")
  print()
  return student_output == actual_output

def has_ifelse(file):
  hasif = False
  haselse = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      line = line.strip()
      if line.startswith("if"):
        hasif = True
      if line.startswith("else"):
        haselse = True
  return hasif and haselse

 
failed = False
 
if not (check_output(student_code) and test1(student_code) and test2(student_code) and test3(student_code) and test4(student_code)) :
  print("<h2>Test did not pass</h2>")
  print("Program did not print the output properly")
  failed = True


if not has_ifelse(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program should use if and else statements")
  failed = True



if not failed:
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)
"""
    with open(os.path.join(".guides", "secure", f"{fname}_helper.py"), "w") as f:
        f.write(helper_code)

    with open(os.path.join("code", f"{fname}.py"), "w") as f:
        pass
    with open(os.path.join(".guides", "secure", "key", f"{fname}_key.py"), "w") as f:
        pass

    with open(os.path.join(".guides", "content", guidePageFname + ".json"), "r+") as f:
        data = json.load(f)
        if hasInput:
            data["files"] = [ {
			"path": "#tabs",
			"action": "close"
		},
		{
			"path": f"code/{fname}.py",
			"panel": 0,
			"action": "open"
		},
		{
			"path": "#terminal: ",
			"panel": 1,
			"action": "open"
		}]
            data["layout"] = "3-cell"
        else:
            data["files"] = [ {
                        "path": "#tabs",
                        "action": "close"
                    },
                    {
                        "path": f"code/{fname}.py",
                        "panel": 0,
                        "action": "open"
                    }
            ]
            data["layout"] = "2-panels"
        f.seek(0)
        json.dump(data, f)

    with open(os.path.join(".guides", "content", guidePageFname + ".md"), "w") as f:
        f.write(f"""Use the button below to test your code before submitting it.

{{Test Code{"| terminal" if hasInput else ""}}}(python3 code/{fname}.py)

{{Check It!|assessment}}({testid})""")

init()
exercise()
