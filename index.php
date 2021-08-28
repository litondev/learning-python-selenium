<!DOCTYPE html>
<html>
	<head>
	</head>
<body>
	<form action="test.php" method="post" id="mypost">
		<input type="text" name="nama">
		<input type="text" name="password">
		<select  name="gender">
			<option value="male">Male</option>
			<option value="female">Female</option>
		</select>	
		<input type="checkbox" name="hobby[]" value="Sleep"> Sleep
		<input type="checkbox" name="hobby[]" value="Eat"> Eat
		<button>Submit</button>
	</form>
	
	<div id="testing">Hello Testing</div>

	<script>
	setTimeout(() => {
		document.getElementById("testing").innerHTML = `
			<div id="testing-id"> Test </div>
		`
	},1000)
	</script>
</body>
</html>