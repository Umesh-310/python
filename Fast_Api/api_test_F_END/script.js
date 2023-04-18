const tesing = async () => {
  const responce = await fetch("http://127.0.0.1:8000/todos/test", {
    method: "POST",
    headers: {
      "content-type": "application/json ",
    },
    body: JSON.stringify({
      username: "umesh8085",
      email: "umeshsaini8085@gmail.com",
      first_name: "umesh",
      last_name: "saini",
      password: "Aku@0310",
    }),
  });
  const data = await responce.json();
  console.log(data);
  return data;
};
console.log("hello");
console.log(tesing());
