<div>
	<span id="nama" value="<?php echo $_POST['nama'];?>-Value"><?php echo $_POST['nama']; ?></span>
	<span id="password" value="<?php echo $_POST['password'];?>-Value"><?php echo $_POST['password'];?></span>
	<span id="gender" value="<?php echo $_POST['gender'];?>-Value"><?php echo $_POST['gender'];?></span>

	<span id="hobby">
	<ul>
		<?php 
		foreach ($_POST['hobby'] as $item) {
			?>	
			<li><?php echo $item;?></li>							
			<?php
		}		
		?>
	</ul>
</div>