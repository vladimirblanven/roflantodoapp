document.getElementById('todo-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const todo = {
        title: document.getElementById('todo-title').value,
        description: document.getElementById('todo-description').value
    };
    fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(todo)
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            addTodoToList(data, 'todo-list');
            document.getElementById('todo-form').reset();
        } else {
            alert(data.error);
        }
    });
});

function addTodoToList(todo, listId) {
    const todoList = document.getElementById(listId);
    const todoItem = document.createElement('div');
    todoItem.classList.add('todo-item');

    const createdAt = new Date(todo.created_at).toLocaleString();

    todoItem.innerHTML = `
        <h4>Created at: ${createdAt}</h4>
        <h2> → ${todo.title}</h2>
        <h4>${todo.description}</h4>
        <button onclick="completeTodo(${todo.id})">Done!</button>
    `;
    todoList.appendChild(todoItem);
}

function loadTodos() {
    fetch('/todos')
    .then(response => response.json())
    .then(data => {
        const todoList = document.getElementById('todo-list');
        todoList.innerHTML = ''; 
        data.forEach(todo => {
            addTodoToList(todo, 'todo-list');
        });
    });
}

function completeTodo(id) {
    fetch(`/todos/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            loadTodos(); 
        } else {
            alert(data.error);
        }
    });
}

function updateDateTime() {
    const now = new Date();
    const currentDate = now.toLocaleDateString();
    const currentTime = now.toLocaleTimeString();
    const season = getSeason(now);
    const dayOfWeek = now.toLocaleDateString('en-US', { weekday: 'long' });
    const leapYear = isLeapYear(now.getFullYear()) ? "Leap Year" : "Not a Leap Year";
    const suggestion = (season === "Spring" || season === "Summer") ? "Go touch grass!" : "Go drink hot cacao!";

    document.getElementById('current-date').textContent = currentDate;
    document.getElementById('current-time').textContent = currentTime;
    document.getElementById('season').textContent = season;
    document.getElementById('day-of-week').textContent = dayOfWeek;
    document.getElementById('leap-year').textContent = leapYear;
    document.getElementById('suggestion').textContent = suggestion;
}

function getSeason(date) {
    const month = date.getMonth() + 1;
    const day = date.getDate();
    if ((month === 3 && day >= 20) || (month > 3 && month < 6) || (month === 6 && day < 21)) return "Spring";
    if ((month === 6 && day >= 21) || (month > 6 && month < 9) || (month === 9 && day < 23)) return "Summer";
    if ((month === 9 && day >= 23) || (month > 9 && month < 12) || (month === 12 && day < 21)) return "Autumn";
    return "Winter";
}

function isLeapYear(year) {
    return ((year % 4 === 0) && (year % 100 !== 0)) || (year % 400 === 0);
}

document.addEventListener('DOMContentLoaded', function() {
    loadTodos();
    updateDateTime();
    setInterval(updateDateTime, 1000);
    setInterval(loadTodos, 30000); 
});