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

module.exports = async function (context, myTimer) {
    var timeStamp = new Date().toISOString()

    if (myTimer.IsPastDue) {
        context.log('JavaScript is running late!')
    }

    con.connect((error) => {
        if (error) throw error
        var sql = `update student set sem = sem + 1 where cpi > 3;`
        con.query(sql, (error, response) => {
            if (error) throw error
            console.log(response.info)
        })
    })

    context.log('Semester updated for students!', timeStamp)

}
