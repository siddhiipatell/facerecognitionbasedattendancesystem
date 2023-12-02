function registration()
{
	var name= document.getElementById("first_name").value;
	var email= document.getElementById("email").value;
	var uname= document.getElementById("last_name").value;
	var pwd= document.getElementById("n_pass").value;
	var c_pwd= document.getElementById("c_pass").value;

        //email id expression code
	var pwd_expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])/;
	var letters = /^[A-Za-z]+$/;
	var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

	if(name=='')
	{
		alert('Please enter your name');
	}
	else if(!letters.test(name))
	{
		alert('Name field required only alphabet characters');
		}
	else if(email=='')
	{
		alert('Please enter your user email id');
		}
	else if (!filter.test(email))
	{
		alert('Invalid email');
	}
	else if(last_=='')
	{
		alert('Please enter the user name.');
	}
	else if(!letters.test(last_name))
	{
		alert('User name field required only alphabet characters');
	}
	else if(n_pass=='')
	{
		alert('Please enter Password');
		}
	else if(c_pass=='')
	{
		alert('Enter Confirm Password');
	}
	else if(!pwd_expression.test(n_pass))
	{
		alert ('Upper case, Lower case, Special character and Numeric letter are required in Password filed');
	}
	else if(n_pass != c_pass)
	{
		alert ('Password not Matched');
	}
	else if(document.getElementById("n_pass").value.length < 6)
	{
		alert ('Password minimum length is 6');
	}
	else if(document.getElementById("n_pass").value.length > 12)
	{
		alert ('Password max length is 12');
	}
	else
	{
	    return false;
	}
}
