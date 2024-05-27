import React, { useEffect, useState } from 'react';

function App() {
    const [todos, setTodos] = useState([]);
    const [description, setDescription] = useState('');

    useEffect(() => {
        fetch('http://localhost:8000/todos/')
            .then(response => response.json())
            .then(data => setTodos(data))
            .catch(error => console.error('Error fetching TODOs:', error));
    }, []);

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('http://localhost:8000/todos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                setTodos([...todos, { description }]);
                setDescription('');
            }
        })
        .catch(error => console.error('Error adding TODO:', error));
    };

    return (
        <div>
            <h1>TODO List</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Enter TODO description"
                />
                <button type="submit">Add TODO</button>
            </form>
            <ul>
                {todos.map((todo, index) => (
                    <li key={index}>{todo.description}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
