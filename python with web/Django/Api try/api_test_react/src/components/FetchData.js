import React from "react";
import { useState } from "react";
const dummy = {
  userName: "",
  className: "",
  age: "",
  studentDetails: "",
};
const dummyUser = {
  username: "",
  password: "",
};
const FetchData = () => {
  const [arr, setArr] = useState([]);
  const [stdInfo, setStdInfo] = useState(dummy);
  const [userInfo, setUserInfo] = useState(dummyUser);
  const [error, setError] = useState("");

  const getData = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/students/");
    if (res.ok) {
      const data = await res.json();
      setArr([...data]);
      console.log(data);
    } else {
      setError({ mes: "GET", val: "data not found" });
    }
  };

  const onClickInput = (event) => {
    setStdInfo({ ...stdInfo, [event.target.name]: event.target.value });
  };

  const onClickUserInput = (event) => {
    setUserInfo({ ...userInfo, [event.target.name]: event.target.value });
  };

  const onSubmitHandler = async (event) => {
    event.preventDefault();
    const token = localStorage.getItem("token");

    try {
      const res = await fetch("http://127.0.0.1:8000/api/addStd/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(stdInfo),
      });
      const data = await res.json();
      setStdInfo(dummy);
      getData();
      if (!res.ok) {
        setError({ mes: "POST", val: data.detail });
      }
    } catch (error) {
      console.log("not working");
      //   const data = await res.json()
      //   console.log(res);
    }
  };

  const onSubmituserToken = async (event) => {
    event.preventDefault();
    const res = await fetch("http://127.0.0.1:8000/api/user/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userInfo),
    });
    if (res.ok) {
      const data = await res.json();
      setUserInfo(dummyUser);
      localStorage.setItem("token", data.access);
    }
    console.log(res);
  };

  const onEdit = (val) => {
    setStdInfo(val);
  };

  const updateHandler = async () => {
    console.log(stdInfo);
    // http://127.0.0.1:8000/api/update/
    await fetch("http://127.0.0.1:8000/api/update/", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(stdInfo),
    });
    getData();
    setStdInfo(dummy);
  };

  const onDelete = async (id) => {
    await fetch("http://127.0.0.1:8000/api/delete/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: id }),
    });
    getData();
  };
  return (
    <div>
      <center>
        <h1>GET Method</h1>
        <button onClick={getData}>get Data</button>
      </center>
      {error.mes === "GET" && <p>{error.val}</p>}
      {arr.map((val) => {
        return (
          <div key={val.id}>
            <b>{val.userName}</b>
            {/* <b>{val.images}</b> */}
            <img src={val.images} alt='images>' />
            <button onClick={() => onEdit(val)}>Edit</button>
            <button onClick={() => onDelete(val.id)}>Delete</button>
          </div>
        );
      })}
      <hr />
      <br />
      <br />
      <center>
        <h1>GET USER refresh & access Token</h1>
        {error.mes === "USER_TOKEN" && <p>{error.val}</p>}
        <form onSubmit={onSubmituserToken}>
          <div>
            <label htmlFor='username'>username : </label>
            <input
              onChange={onClickUserInput}
              type='text'
              value={userInfo.username}
              name='username'
              id='username'
            />
          </div>
          <div>
            <label htmlFor='password'>password : </label>
            <input
              onChange={onClickUserInput}
              type='password'
              value={userInfo.password}
              autoComplete='on'
              name='password'
              id='password'
            />
          </div>
          <input type='submit' />
        </form>
      </center>
      <br />
      <hr />
      <br />
      <br />
      <center>
        <h1>POST Method</h1>
        {error.mes === "POST" && <p>{error.val}</p>}
        <form onSubmit={onSubmitHandler}>
          <div>
            <label htmlFor='username'>username : </label>
            <input
              type='text'
              value={stdInfo.userName}
              onChange={onClickInput}
              name='userName'
              id='user'
            />
          </div>
          <br />
          <div>
            <label htmlFor='className'>className : </label>
            <input
              type='text'
              value={stdInfo.className}
              onChange={onClickInput}
              name='className'
              id='className'
            />
          </div>
          <br />
          <div>
            <label htmlFor='age'>Age : </label>
            <input
              type='text'
              value={stdInfo.age}
              onChange={onClickInput}
              name='age'
              id='age'
            />
          </div>
          <br />
          <div>
            <label htmlFor='studentDetails'>studentDetails : </label>
            <input
              type='text'
              value={stdInfo.studentDetails}
              onChange={onClickInput}
              name='studentDetails'
              id='studentDetails'
            />
          </div>
          <br />
          {stdInfo.id && (
            <>
              <button onClick={updateHandler}>Update</button>{" "}
              <button onClick={() => setStdInfo(dummy)}>Cencel</button>
            </>
          )}
          {!stdInfo.id && <input type='submit' />}
        </form>
      </center>
    </div>
  );
};

export default FetchData;

// http://127.0.0.1:8000/api/register/
