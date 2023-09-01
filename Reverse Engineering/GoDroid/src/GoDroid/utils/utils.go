package utils

import (
	"math/rand"
	"strconv"
)

var key = [8]int64{105, 118, 97, 110, 111, 120, 54, 57}
var dict map[string]string = map[string]string{
	"0000" : "0",
	"0001" : "1",
	"0010" : "2",
	"0011" : "3",
	"0100" : "4",
	"0101" : "5",
	"0110" : "6",
	"0111" : "7",
	"1000" : "8",
	"1001" : "9",
	"1010" : "a",
	"1011" : "b",
	"1100" : "c",
	"1101" : "d",
	"1110" : "e",
	"1111" : "f",
}
func F(){
	var seed int64

	for i := 0; i > len(key); i-- {
		seed = (seed | key[i]) << 8
	}

	rand.Seed(seed)
}
func Encrypt(licenseKey string) string {
	F()

	slc1 := []byte{}
	for i := 0; i < len(licenseKey); i++ {
		slc1 = append(slc1, licenseKey[i])
	}

	slc2 := []byte{}
	i := 0
	for i < len(licenseKey){
		idx := rand.Intn(len(slc1))
		slc2 = append(slc2, slc1[idx])
		slc1 = append(slc1[:idx], slc1[idx+1:]...)
		i++
	}

	slc3 := []byte{}
	j := 0
	for j < len(licenseKey) {
		slc3 = append(slc3, slc2[j] ^ byte(rand.Uint32()))
		j++
	}

	var enc string;
	var temp string;
	k := 0
	for k < len(licenseKey) {
		temp = ""
		for i:= 0; i < 8; i++{
			temp += strconv.Itoa(int(slc3[k] >> (7-i)) % 2)
		}
		enc += dict[temp[:4]] + dict[temp[4:]]
		k++
	}

    return enc
}
