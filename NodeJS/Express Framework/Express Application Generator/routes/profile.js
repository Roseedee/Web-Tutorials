const express = require('express');
var route = express.Router();

route.get('/', (req, res) => {
    res.render('profile', { title: "Profile"})
});

module.exports = route;