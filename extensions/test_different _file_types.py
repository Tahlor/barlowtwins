from torchvision.datasets.folder import pil_loader

path = "/home/taylor/anaconda3/FRENCH_CENSUS/61882_b940293-00457.j2k"

img = pil_loader(path)
img.show()

for ext in ".dds",".dib",".j2k",".im",".msp",".pcx",".sgi",".tga",".xbm",".spider":
    try:
        if
        img.save(f"test_file{ext}", )
        new_img = pil_loader("test_file" + ext)
        img.show()
    except Exception as e:
        print(f"{ext} failed")
        print(e)
