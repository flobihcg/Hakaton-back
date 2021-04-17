if(!file_exists('counter.txt')){
    file_put_contents('counter.txt', '0');
}
file_put_contents('counter.txt', ((int) file_get_contents('counter.txt')) + 1);
header('Location: ' . $_GET['href']);