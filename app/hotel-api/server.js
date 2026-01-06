const express = require("express");
const app = express();

app.get("/health", (req, res) => res.send("OK"));

app.get("/hotels", (req, res) => {
  const delay = Math.floor(Math.random() * 500);
  setTimeout(() => {
    res.json({
      hotel: "Azure Grand",
      price: 4500,
      delay
    });
  }, delay);
});

app.listen(3001, () => {
  console.log("Hotel API running on port 3001");
});
