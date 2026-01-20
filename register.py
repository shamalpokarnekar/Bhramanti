#!C:\python312\python.exe
import cgi
import cgitb
import header
cgitb.enable()
#print("Content-Type:text/html\n")
print(''' 
<doctype>
<html>
<head>
<style>  
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Montserrat', sans-serif;
}
body{
 
  background:
  padding: 0 10px;
}
.wrapper{
  max-width: 500px;
  width: 100%;
  background: #fff;
  margin: 50px auto;
  box-shadow: 2px 3px 4px rgba(0,0,0,0.125);
  padding: 30px;
}

.wrapper .title{
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 25px;
  color: #fec107;
  text-transform: uppercase;
  text-align: center;
}

.wrapper .box{
  width: 100%;
}

.wrapper .box .inputfield{
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}

.wrapper .box .inputfield label{
   width: 200px;
   color: #757575;
   margin-right: 10px;
  font-size: 14px;
}

.wrapper .box .inputfield .input,
.wrapper .box .inputfield .textarea{
  width: 100%;
  outline: none;
  border: 1px solid #d5dbd9;
  font-size: 15px;
  padding: 8px 10px;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.wrapper .box .inputfield .textarea{
  width: 100%;
  height: 125px;
  resize: none;
}

.wrapper .box .inputfield .custom_select{
  position: relative;
  width: 100%;
  height: 37px;
}

.wrapper .box .inputfield .custom_select:before{
  content: "";
  position: absolute;
  top: 12px;
  right: 10px;
  border: 8px solid;
  border-color: #d5dbd9 transparent transparent transparent;
  pointer-events: none;
}

.wrapper .box .inputfield .custom_select select{
  -webkit-appearance: none;
  -moz-appearance:   none;
  appearance:        none;
  outline: none;
  width: 100%;
  height: 100%;
  border: 0px;
  padding: 8px 10px;
  font-size: 15px;
  border: 1px solid #d5dbd9;
  border-radius: 3px;
}


.wrapper .box .inputfield .input:focus,
.wrapper .box .inputfield .textarea:focus,
.wrapper .box .inputfield .custom_select select:focus{
  border: 1px solid #fec107;
}

.wrapper .box .inputfield p{
   font-size: 14px;
   color: #757575;
}
.wrapper .box .inputfield .check{
  width: 15px;
  height: 15px;
  position: relative;
  display: block;
  cursor: pointer;
}
.wrapper .box .inputfield .check input[type="checkbox"]{
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}
.wrapper .box .inputfield .check .checkmark{
  width: 15px;
  height: 15px;
  border: 1px solid #fec107;
  display: block;
  position: relative;
}
.wrapper .box.inputfield .check .checkmark:before{
  content: "";
  position: absolute;
  top: 1px;
  left: 2px;
  width: 5px;
  height: 2px;
  border: 2px solid;
  border-color: transparent transparent #fff #fff;
  transform: rotate(-45deg);
  display: none;
}
.wrapper .box .inputfield .check input[type="checkbox"]:checked ~ .checkmark{
  background: #fec107;
}

.wrapper .box .inputfield .check input[type="checkbox"]:checked ~ .checkmark:before{
  display: block;
}

.wrapper .box .inputfield .btn{
  width: 100%;
   padding: 8px 10px;
  font-size: 15px; 
  border: 0px;
  background:  #fec107;
  color: #fff;
  cursor: pointer;
  border-radius: 3px;
  outline: none;
}

.wrapper .box .inputfield .btn:hover{
  background: #ffd658;
}

.wrapper .box .inputfield:last-child{
  margin-bottom: 0;
}

@media (max-width:420px) {
  .wrapper .box .inputfield{
    flex-direction: column;
    align-items: flex-start;
  }
  .wrapper .box .inputfield label{
    margin-bottom: 5px;
  }
  .wrapper .box .inputfield.terms{
    flex-direction: row;
  }
}
</style>
</head>
<body>

<div class="wrapper">
    <div class="title">
      Registration Form
    </div>
            <form action="registerback.py" method="POST">

    <div class="box">
       <div class="inputfield">
          <label>Name</label>
          <input type="text" name="name" id="name" class="input">
       </div>  <br>
       <div class="inputfield">
          <label>Phone No</label>
          <input type="tel" name="pn" id="pn" class="input">
       </div><br>
       <div class="inputfield">
          <label>Email Address</label>
          <input type="text" name="email" id="email"class="input">
       </div> <br>
       <div class="inputfield">
          <label>Password</label>
          <input type="password" name="password" id="password" class="input">
       </div>  
             
        <br>
      
      <div class="inputfield">
        <input type="submit" value="Register" class="btn">
      </div>
    </div>
    </form>
</div>
</body>
</html>
''')
import footer