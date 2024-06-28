const express = require("express");
const app = express();
app.use(express.json());
app.use(express.static("public"));
app.get("/user/dashboard/:id",(req,res)=>{
    console.log(req.params);
    console.log(req.body);
    res.json({
        name:"Pratham Doshi"
    })
});
app.listen(3000,()=>{
    console.log(`Server Started at http://localhost:3000`);
})