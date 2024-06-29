import React from 'react';
import { Link } from 'react-router-dom';
import './Navigation.css'

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/create-diet-plan">Create Diet Plan</Link>
        </li>
        {/* Add other navigation links as needed */}
      </ul>
    </nav>
  );
};

export default Navigation;
