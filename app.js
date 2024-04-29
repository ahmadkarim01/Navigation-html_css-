// Define UI Vars
const form = document.querySelector('#task-form');
const taskLisht = document.querySelector('.collection');
const clearBtn = document.querySelector('.clear-tasks');
const filter = document.querySelector('#filter');
const taskInput = document.querySelector('#task');
// load all event listeners
loadEventListeners();

//LOad all event listeners;
function loadEventListeners() {
    //Add task event
    form.addEventListener('submit', addTask);
}

//Add task
function addTask(e) {
    If(taskInput.value === ('') {
        alert('Add a task');
    }
    // Create li element
    const li = document.createElement('li');
    //Add class
    li.className = 'collection-item';
    //create text node and appent to li
    li.appendChild(document.createTextNode(taskInput.value));
    //create new link element
    const link = document.createElement('a');
    //Add class
    link.className = 'delete-item secondary-content';
    //add icon html
    link.innerHTML = <i class = "fa fa-remove"></i>;
    //Append the link to li
    li.appendChild(link);
    //append li to ul
    taskList.appendChild(li);

    //clear input
    taskInput.value = '';

    e.preventDefault();
}