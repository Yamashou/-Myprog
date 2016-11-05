package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	url := "https://notify-api.line.me/api/notify"

	resp, _ := http.Get(url)
	defer resp.Body.Close()

	byteArray, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(byteArray)) // htmlをstringで取得
}
