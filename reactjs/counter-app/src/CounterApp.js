import React, {useState} from 'react';
import PropTypes from 'prop-types';


const Counterapp = ({ value = 10 }) => {

  const [counter, setCounter] = useState(value);

  const handleAdd = (e) => setCounter(counter + 1);
  const handleReset = (e) => setCounter(value);
  const handleSubtract = (e) => setCounter(counter - 1);

  return (
    <>
      <h1>Counter App</h1>
      <p>{counter}</p>
      <button onClick={handleAdd}>+1</button>
      <button onClick={handleReset}>Reset</button>
      <button onClick={handleSubtract}>-1</button>
    </>
  );
};

Counterapp.propTypes = {
  counter: PropTypes.number,
};

export default Counterapp;