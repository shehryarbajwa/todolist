
//Create new task
  const descInput = document.getElementById('description');
  const titleInput = document.getElementById('title')
  const dateInput = document.getElementById('date')

  document.getElementById('form-create').onsubmit = function (e) {
    e.preventDefault();
    const desc = descInput.value;
    const title = titleInput.value;
    const date = dateInput.value;

    descInput.value = '';
    titleInput.value = '';
    dateInput.value = '';

    fetch('/todos/create', {
      method: 'POST',
      body: JSON.stringify({

        'title': title,
        'description': desc,
        'date': date
      }),
      headers: {
        'Content-Type': 'application/json',
      }
    })
      .then(response => response.json())
      .then(jsonResponse => {
        const li = document.createElement('li');
        const checkbox = document.createElement('input');
        checkbox.className = 'check-completed';
        checkbox.type = 'checkbox';
        checkbox.setAttribute('data-id', jsonResponse.id);
        console.log(jsonResponse.id)
        li.appendChild(checkbox);

        const text = document.createTextNode(' Title: ' + title + ' Description: ' + desc + ' Due-date: ' + date + ' ');

        li.appendChild(text);

        const deleteBtn = document.createElement('button');
        const editBtn = document.createElement('button');
        editBtn.className = 'edit-button';
        deleteBtn.className = 'delete-button';
        editBtn.setAttribute('data-id', jsonResponse.id);
        deleteBtn.setAttribute('data-id', jsonResponse.id);

        editBtn.innerHTML = 'Edit'
        deleteBtn.innerHTML = 'Delete;';
        li.appendChild(deleteBtn);
        li.appendChild(editBtn)

        document.getElementById('todos').appendChild(li);
      })
      .catch(function () {
        console.error('Error occurred');
      })
  }

  // Task Completed
  const checkboxes = document.querySelectorAll('.check-completed');
  for (let i = 0; i < checkboxes.length; i++) {
    const checkbox = checkboxes[i];
    checkbox.onchange = function (e) {
      console.log('Hello world completed')
      const newCompleted = e.target.checked;
      const todoId = e.target.dataset['id'];
      fetch('/todos/' + todoId + '/completed', {
        method: 'POST',
        body: JSON.stringify({
          'completed': newCompleted
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(function () {
          document.getElementById('error').className = 'hidden';
        })
        .catch(function () {
          document.getElementById('error').className = '';
        })
    }
  }

  // Delete Task
  const deleteBtns = document.querySelectorAll('.delete-button');
  for (let i = 0; i < deleteBtns.length; i++) {
    const btn = deleteBtns[i];
    btn.onclick = function (e) {
      const todoId = e.target.dataset['id'];
      fetch('/todos/' + todoId, {
        method: 'DELETE'
      })
        .then(function () {
          const item = e.target.parentElement;
          item.remove();
        })
    }
  }
  // Edit task
  

  const editBts = document.querySelectorAll('.edit-button');
  for (let i = 0; i < editBts.length; i++) {
    const btn = editBts[i];
    btn.onclick = function (e) {
      const todoId = e.target.dataset['id'];
      e.preventDefault()
      var editdiv = document.getElementById('edit_tasks');
      if (editdiv.style.display === 'block'){
        editdiv.style.display = 'none'
      } else {
        editdiv.style.display = 'block'
      }
      var x = document.getElementById("form-edit");
      if (x.style.display === "block") {
        x.style.display = "none";
      } else {
        x.style.display = "block";
      }
      document.getElementById('form-edit').onsubmit = function (e) {
        e.preventDefault()

        var titleValue = document.getElementById('title_edit').value
        var descriptionValue = document.getElementById('description_edit').value
        var dateValue = document.getElementById('date_edit').value

        fetch('/todos/' + todoId, {
          method: 'PATCH',
          body: JSON.stringify({
            'title': titleValue,
            'description': descriptionValue,
            'date': dateValue
          }),
          headers: {
            'Content-Type': 'application/json',
          }
        })
          .then(response => response.json())
          .then(jsonResponse => {
            x.style.display = 'none'
            editdiv.style.display = 'none'
          })
      }

    }
  }
