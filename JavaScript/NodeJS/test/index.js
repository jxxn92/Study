const express = require('express');
const app = express();

app.get('/', function (req, res) {
    res.send('Hello World');
});

app.get('/sound/:name', function (req, res) {
    const { name } = req.params;

    if (name == 'dog') {
        res.json({ sound: '멍멍' });
    } else if (name == 'cat') {
        res.json({ sound: '냐옹' });
    } else if (name == 'pig') {
        res.json({ sound: '꿀꿀' });
    } else {
        res.json({ sound: '알수 없음' });
    }

    // res.send('Hello World');
});

app.listen(3000);
