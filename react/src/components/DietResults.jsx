import React from 'react';
import { useNavigate } from 'react-router-dom';
import './DietResult.css';

const DietResults = () => {
  const userData = JSON.parse(localStorage.getItem('userData'));
  const navigate = useNavigate();

  if (!userData) {
    navigate('/');
    return null;
  }

  const { name, age, weight, height, goal } = userData;

  const getDietRecommendation = () => {
    if (goal === 'Lose Weight') {
      return 'Low-carb, high-protein diet';
    } else if (goal === 'Maintain Weight') {
      return 'Balanced diet with moderate portions';
    } else if (goal === 'Gain Weight') {
      return 'High-calorie, nutrient-dense diet';
    }
  };

  return (
    <div className="results-container">
      <h2>Diet Recommendation for {name}</h2>
      <p>Age: {age}</p>
      <p>Weight: {weight} kg</p>
      <p>Height: {height} cm</p>
      <p>Goal: {goal}</p>
      <h3>Recommended Diet: {getDietRecommendation()}</h3>
    </div>
  );
};

export default DietResults;
