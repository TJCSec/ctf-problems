<!DOCTYPE html>
<html>
    <head>
        <title>Image It - Home</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">
        <style>
            body > .container
            {
                padding: 60px 15px 0;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Image It</a>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="index.php">Home</a></li>
                        <li class="active"><a href="upload.php">Upload</a></li>
                    </ul>
                </div><!--/.nav-collapse -->
            </div>
        </nav>
        <div class="container">
            <div class="page-header">
                <h2>Upload an Image</h2>
            </div>
            <?php
            function generateRandomString($length = 10) {
                $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
                $randomString = '';
                for ($i = 0; $i < $length; $i++) {
                    $randomString .= $characters[rand(0, strlen($characters) - 1)];
                }
                return $randomString;
            }
            if(isset($_FILES["file"])){
                $name = basename($_FILES["file"]["name"]);
                $extension = pathinfo($name,PATHINFO_EXTENSION); // Make sure to copy extension so it works
                $path = "uploads/" . generateRandomString(30) . "." . $extension;// Rename file so people can't overwrite other images
                $allowed_types = array(IMAGETYPE_PNG, IMAGETYPE_JPEG, IMAGETYPE_GIF); // Make sure people don't upload malicious files
                $ok = 1;

                if($_FILES["file"]["size"] > 2000000){
                    echo '<div class="alert alert-danger" role="alert">Image is too big.</div>';
                    $ok = 0;
                }

                if(!in_array(exif_imagetype($_FILES["file"]["tmp_name"]),$allowed_types)){
                    echo '<div class="alert alert-danger" role="alert">Image is not a PNG, JPEG, or GIF.</div>';
                    $ok = 0;
                }

                if(file_exists($path)){
                    echo '<div class="alert alert-danger" role="alert">Uh... the image exists already.</div>';
                    $ok = 0;
                }
                
                if($ok == 1){
                    if(move_uploaded_file($_FILES["file"]["tmp_name"], $path)){
                        echo '<p>Your image has been uploaded at <a href="'.$path.'">'.$path.'</a>. Thanks for using Image It!';
                    }
                    else {
                        echo '<div class="alert alert-danger" role="alert">Something happened during the upload.</div>';
                    }
                }
            }
            else {
                echo '<form action="upload.php" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="file">Image:</label>
                <input class="form-control" type="file" name="file" id="file">
            </div>
            <button class="btn btn-primary" type="submit">Upload</button>
            </form>';
            }
            ?>
        </div>
        <script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    </body>
</html>
