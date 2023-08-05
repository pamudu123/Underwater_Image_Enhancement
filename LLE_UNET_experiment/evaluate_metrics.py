'''
The DatasetMetrics class provides methods to calculate and update average evaluation metrics 
(PSNR, SSIM, MSE) for a dataset of image pairs. It keeps track of the total scores and the 
number of processed images to compute the averages. 
'''

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


class DatasetMetrics:
    def __init__(self):
        self.total_psnr = 0
        self.total_ssim = 0
        self.total_mse  = 0
        self.total_images = 0

    def update_metrics(self, img1, img2):
        mse_score = self.calculate_mse(img1, img2)
        psnr = self.calculate_psnr(img1, img2)
        ssim_score = self.calculate_ssim(img1, img2)

        self.total_psnr += psnr
        self.total_ssim += ssim_score
        self.total_mse += mse_score
        self.total_images += 1
        
    def calculate_mse(self, img1, img2):
        return np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    
    def calculate_psnr(self, img1, img2,max_pixel=1.0):
        mse = self.calculate_mse(img1, img2)
        if mse == 0:
            return 100
        psnr = 20 * np.log10(max_pixel / (np.sqrt(mse)))
        return psnr
    
    def calculate_ssim(self, img1, img2):
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        return ssim(gray1, gray2,data_range= 1-0)

    def __str__(self):
        if self.total_images == 0:
            return "No images processed yet."
        
        avg_psnr = self.total_psnr / self.total_images
        avg_ssim = self.total_ssim / self.total_images
        avg_mse = self.total_mse / self.total_images

        return f"Average PSNR: {avg_psnr:.4f}, Average SSIM: {avg_ssim:.4f}, Average MAE: {avg_mse:.4f}"

# # Usage example:
# if __name__ == "__main__":
#     # Assuming you have a list of image pairs, img_list1 and img_list2
#     dataset_metrics = DatasetMetrics()

#     for img1, img2 in zip(img_list1, img_list2):
#         dataset_metrics.update_metrics(img1, img2)

#     print(dataset_metrics)