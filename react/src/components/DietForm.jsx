import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './DietForm.css';

const DietForm = () => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [goal, setGoal] = useState('Lose Weight');
  const [foodtype, setFoodType] = useState('Vegetarian');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const userData = { name, age, weight, height, goal };
    localStorage.setItem('userData', JSON.stringify(userData));
    navigate('/results');
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="diet-form">
        <h2>Get Your Diet Plan</h2>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Weight (kg)"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          required
        />
        <input
          type="number"
          placeholder="Height (cm)"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          required
        />
        <select value={goal} onChange={(e) => setGoal(e.target.value)} required>
          <option value="Lose Weight">Lose Weight</option>
          <option value="Maintain Weight">Maintain Weight</option>
          <option value="Gain Weight">Gain Weight</option>
        </select>
        <select value={foodtype} onChange={(e) => setFoodType(e.target.value)} required>
          <option value="Vegetarian">Vegetarian</option>
          <option value="Non-Vegetarian">Non-Vegetarian</option>
        </select>
        <button type="submit">Get Recommendation</button>
      </form>
    </div>
  );
};

export default DietForm;
