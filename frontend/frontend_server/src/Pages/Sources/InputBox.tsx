import React, { ChangeEvent } from 'react'

interface InputBoxProps {
    type?: string;
    name: string;
    value: string;
    placeholder: string;
    onChange: (event: ChangeEvent<HTMLInputElement>) => void;
  }
  
  const InputBox: React.FC<InputBoxProps> = ({ type = 'text', name, value, placeholder, onChange }) => {
    return (
      <>
      <input
        type={type}
        name={name}
        className="input-box"
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
      </>
    );
};

export default InputBox;