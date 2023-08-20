import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def create_grid(images_info, rows, cols,save_img_name):
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
    
    
    plt.savefig(save_img_name, dpi=300)
    plt.show()

<<<<<<< HEAD
# List of image data (path,title)
=======
# List of image data (path, row, col, title)
folder_name = 'IMG_800'

>>>>>>> 32d75e7 (add new results)
image_data = [
    (f"layer_outputs/{folder_name}/block1_pool.png", "1"),
    (f"layer_outputs/{folder_name}/block1_conv2.png","5"),
    (f"layer_outputs/{folder_name}/concatenate_4.png","10"),

    (f"layer_outputs/{folder_name}/block1_pool.png", "2"),
    (f"layer_outputs/{folder_name}/block1_conv2.png","6"),
    (f"layer_outputs/{folder_name}/concatenate_4.png","11"),

    (f"layer_outputs/{folder_name}/block1_pool.png", "3"),
    (f"layer_outputs/{folder_name}/block1_conv2.png","7"),
    (f"layer_outputs/{folder_name}/concatenate_4.png","12"),

    (f"layer_outputs/{folder_name}/block1_pool.png", "4"),
    (f"layer_outputs/{folder_name}/block1_conv2.png","8"),
    (f"layer_outputs/{folder_name}/concatenate_4.png","13"),

    ("NAN", ""),
    (f"layer_outputs/{folder_name}/block1_conv2.png","9"),
    ("NAN",""),

]


rows = 5
cols = 3
save_name = f"layer_outputs/{folder_name}/{folder_name}_Layers.png"
create_grid(image_data, rows, cols,save_name)
