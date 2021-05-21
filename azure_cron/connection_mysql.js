var mysql = require('mysql2')

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'university'
})

con.connect(function (error) {
    if (error) throw error
    console.log('Connected!')
})

con.connect((error) => {
    if (error) throw error
    var sql = `select student_id, first_name from student`
    con.query(sql, (error, response) => {
        if (error) throw error
        console.log(response)
    })
})
