from main import main
sample = [["https://images-na.ssl-images-amazon.com/images/G/01/digital/video/hero/TVSeries/Friends_4926700-FRIENDS._V392939166_SX1080_.jpg","https://www.biography.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_768/MTcxNDEzMTU5NzM3ODI5MzU4/rachel-haircut-gettyimages-138427199.jpg","https://pyxis.nymag.com/v1/imgs/079/792/3ed0d94be0a9bd3d023f00532889bab152-30-chandler-bing.rsquare.w330.jpg"],["Rachel","Chandler"]]

print(main().predict(sample, ["feature_name"]))
