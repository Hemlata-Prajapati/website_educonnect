function viewAssignment(btn){

let id = btn.dataset.id
let title = btn.dataset.title
let description = btn.dataset.description
let due = btn.dataset.due
let questions = btn.dataset.questions
let pdf = btn.dataset.pdf
let submitted = btn.dataset.submitted   // ✅ NEW

document.getElementById("modalTitle").innerText = title
document.getElementById("modalDescription").innerText = description
document.getElementById("modalDue").innerText = due

let questionHtml = ""
let answerHtml = ""

// ✅ अगर already submit किया है
if(submitted === "yes"){

    document.getElementById("modalQuestions").innerHTML =
    "<p style='color:green;font-weight:600;'>✅ Your assignment is submitted</p>"

    document.getElementById("modalAnswers").innerHTML = ""

    document.getElementById("submitForm").style.display = "none"

}
else{

    if(questions){

        let qList = questions.split("||")
        let index = 1

        qList.forEach(q => {

            if(q.trim() !== ""){

                questionHtml += "<p><b>"+ q +"</b></p>"

                answerHtml += `
                <div style="margin-bottom:15px">
                <label>Answer ${index}</label>
                <textarea name="answers[]" rows="3"
                style="width:100%;padding:8px;border:1px solid #ccc;border-radius:6px"></textarea>
                </div>
                `

                index++

            }

        })

    }

    document.getElementById("modalQuestions").innerHTML = questionHtml
   document.getElementById("modalAnswers").innerHTML = answerHtml;

// 👇 NEW (force refresh inputs)
document.querySelectorAll("#modalAnswers textarea").forEach(el => {
    el.value = "";
});

    document.getElementById("submitForm").style.display = "block"

}

// PDF handling
if(pdf && pdf.trim() !== ""){
    document.getElementById("pdfFile").innerHTML =
    `<p><b>Assignment File:</b> <a href="${pdf}" target="_blank">Download PDF</a></p>`
}
else{
    document.getElementById("pdfFile").innerHTML = ""
}

// form action
document.getElementById("submitForm").action =
`/student/assignments/${id}/submit/`;
console.log("FORM ACTION:", document.getElementById("submitForm").action)
// modal open
document.getElementById("assignmentModal").style.display="block"

}

function closeModal(){
document.getElementById("assignmentModal").style.display="none"
}

