const express = require('express');

const router = express.Router();

let data = [
    {
        id: 1,
        name: "Roseedee",
        age: 21
    },
    {
        id: 2,
        name: "Solahudeen",
        age: 20
    }
]

router.get('/', (req, res) => {
    res.json(data);
})

module.exports = router;