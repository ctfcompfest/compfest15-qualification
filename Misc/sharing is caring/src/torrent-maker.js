import createTorrent from 'create-torrent'
import fs from 'fs'

createTorrent("./hippity_hop/",{
	pieceLength:12 ,
	private: true,
	announceList : [["COMPFEST15{Y0u_re4lLy_thOUght_th3_flAG_w4s_h3re_don't_ya! Ha! b3tter_lUcK_n3xT_t1me!}"]],
	urlList : [["https://www.youtube.com/watch?v=nXbQlYKya5E","https://www.youtube.com/watch?v=gsNUS7PaAP0"]],
},(err, torrent) => {
	if (!err) {
		fs.writeFile("wibu", torrent, (err, res) => {
			if(err) console.log(err);
		})
		}
		else{
			console.log(err);
		}
})