import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def create_grid(images_info, rows, cols):
    fig, axes = plt.subplots(rows, cols, figsize=(16, 12))
    plt.subplots_adjust(wspace=0.1, hspace=0.2)
    
    for row in range(rows):
        for col in range(cols):
            ax = axes[row, col]
            ax.axis('off')
            
            index = row * cols + col
            if index < len(images_info):
                image_path, title = images_info[index]
                try:
                    image = mpimg.imread(image_path)
                except FileNotFoundError:
                    # If image not found, create a white image
                    image = np.ones((100, 100, 3), dtype=np.uint8) * 255
                
                ax.imshow(image)
                ax.set_title(title)
    
    
    plt.savefig('layes.png', dpi=300)
    plt.show()

# List of image data (path, , title)
image_data = [
    ("layer_outputs/block1_pool.png", "1"),
    ("layer_outputs/block1_conv2.png","5"),
    ("layer_outputs/concatenate_4.png","10"),

    ("layer_outputs/block1_pool.png", "2"),
    ("layer_outputs/block1_conv2.png","6"),
    ("layer_outputs/concatenate_4.png","11"),

    ("layer_outputs/block1_pool.png", "3"),
    ("layer_outputs/block1_conv2.png","7"),
    ("layer_outputs/concatenate_4.png","12"),

    ("layer_outputs/block1_pool.png", "4"),
    ("layer_outputs/block1_conv2.png","8"),
    ("layer_outputs/concatenate_4.png","13"),

    ("NAN", ""),
    ("layer_outputs/block1_conv2.png","9"),
    ("NAN",""),

]


rows = 5
cols = 3
create_grid(image_data, rows, cols)
