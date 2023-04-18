// const dataApi = async () => {
//   const res = await fetch("http://127.0.0.1:8000/api/students/");
//   // if (res.ok) {
//   const data = await res.json();
//   console.log(data);
//   // }
// };

// dataApi();
// // http://127.0.0.1:5500/api_test_frontend/index.html

let form = document.getElementById("login-form");

console.log(form);

form.addEventListener("submit", (e) => {
  e.preventDefault();

  let fromData = {
    username: from.username.value,
    password: from.password.value,
  };

  console.log(fromData);
});
