import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import DietForm from './components/DietForm';
import DietResults from './components/DietResults';
import Header from './components/Header';
import Footer from './components/Footer';
import './styles/global.css';
import Navigation from './components/Navigation';
import CreateDietPlan from './components/CreateDietPlan';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<DietForm />} />
            <Route path="/create-diet-plan" element={<CreateDietPlan />} />
            
            <Route path="/results" element={<DietResults />} />

          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
