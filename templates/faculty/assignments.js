window.onload = function() {
    document.getElementById("successModal").style.display = "block";
}

function openModal(){
document.getElementById("assignmentModal").style.display="block";
}

function closeModal(){
document.getElementById("assignmentModal").style.display="none";
}


function goToStep2(){
document.getElementById("step1").style.display="none";
document.getElementById("step2").style.display="block";

document.getElementById("modalTitle").innerText="Create Questions";
}
function goBack(){

document.getElementById("step2").style.display="none";
document.getElementById("step1").style.display="block";

}

let questionCount = 1;

function addQuestion(){

questionCount++;

let container = document.getElementById("questionsContainer");

let html = `
<div class="question-box">

<label>Question ${questionCount}</label>
<input type="text" name="questions[]" placeholder="Enter Question">

</div>
`;

container.insertAdjacentHTML("beforeend", html);

}
function openConfirmModal(){
document.getElementById("confirmModal").style.display="block";
}

function closeConfirmModal(){
document.getElementById("confirmModal").style.display="none";
}

function submitAssignment(){

document.getElementById("confirmModal").style.display="none";

document.getElementById("assignmentForm").submit();

}
function closeSuccessModal(){
    document.getElementById("successModal").style.display="none";
}
function openDeleteModal(id){

document.getElementById("deleteModal").style.display="block";

document.getElementById("confirmDeleteBtn").href =
"{% url 'delete_assignment' 0 %}".replace("0", id);

}

function closeDeleteModal(){

document.getElementById("deleteModal").style.display="none";

}

