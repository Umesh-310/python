import React, { useState } from "react";

const dummyUser = {
  username: "",
  password: "",
  password2: "",
  email: "",
  first_name: "",
  last_name: "",
};

const CreateUser = () => {
  const [userInfo, setUserInfo] = useState(dummyUser);

  const onClickInput = (event) => {
    setUserInfo({ ...userInfo, [event.target.name]: event.target.value });
  };

  const onSubmitHandler = async (event) => {
    event.preventDefault();

    const res = await fetch("http://127.0.0.1:8000/api/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userInfo),
    });
    const data = await res.json();
    console.log(data);
  };

  return (
    <div>
      <center>
        <h1>Create user Method</h1>
        <form onSubmit={onSubmitHandler}>
          <div>
            <label htmlFor='username'>Username : </label>
            <input
              type='text'
              onChange={onClickInput}
              name='username'
              id='user'
            />
          </div>
          <br />
          <div>
            <label htmlFor='password'>Password : </label>
            <input
              type='password'
              onChange={onClickInput}
              name='password'
              id='password'
            />
          </div>
          <br />
          <div>
            <label htmlFor='password2'>Password2 : </label>
            <input
              type='password'
              onChange={onClickInput}
              name='password2'
              id='password2'
            />
          </div>
          <br />
          <div>
            <label htmlFor='email'>Email : </label>
            <input
              type='email'
              onChange={onClickInput}
              name='email'
              id='email'
            />
          </div>
          <br />
          <div>
            <label htmlFor='firstname'>First Name : </label>
            <input
              type='text'
              onChange={onClickInput}
              name='first_name'
              id='firstname'
            />
          </div>
          <br />
          <div>
            <label htmlFor='lastname'>Last Name : </label>
            <input
              type='text'
              onChange={onClickInput}
              name='last_name'
              id='lastname'
            />
          </div>
          <br />
          <input type='submit' />
        </form>
      </center>
    </div>
  );
};

export default CreateUser;
