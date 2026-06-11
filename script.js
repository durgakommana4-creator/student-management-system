// Add Student
function addStudent() {

    let name = document.getElementById("name").value;

    let age = document.getElementById("age").value;

    fetch("/add_student", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            name: name,
            age: age
        })

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadStudents();

    });

}


// Load Students
function loadStudents() {

    fetch("/students")

    .then(response => response.json())

    .then(data => {

        let studentList = document.getElementById("studentList");

        studentList.innerHTML = "";

        data.forEach(student => {

            studentList.innerHTML += `
                <li>
                    ${student.name} - ${student.age}
                </li>
            `;
        });

    });

}

loadStudents();