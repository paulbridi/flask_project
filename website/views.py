from flask import Blueprint, render_template, request, redirect, url_for, flash
import openai
openai.api_key = "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"


views = Blueprint('views', __name__)

@views.route('/', methods=["POST","GET"])
def home():
    local_instruction = "Give fun spontaneous weekend plans"
    if request.method == "POST":
        i_string = request.form["input-string"]
        print(i_string)

        oai_object = openai.Edit.create(
            # Feed the openai model the string inputted by the user
            model="text-davinci-edit-001",
            input=i_string,
            instruction=local_instruction
            )

        # print(oai_object.instruction)
        # instruction_gvent = oai_object.instruction

        o_string = oai_object["choices"][0]["text"]

        return render_template("home.html", i_string=i_string,  o_string=o_string, local_instruction=local_instruction)
    else:
        return render_template("home.html", local_instruction=local_instruction)
