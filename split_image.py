import cv2
import os

def slice_and_save_images(folder_path, grid_size):
    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Iterate over each image file
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read the image '{image_file}'. Skipping...")
            continue
        
        # Get the dimensions of the image
        height, width, _ = image.shape
        
        # Calculate the size of each grid cell
        cell_height = height // grid_size[0]
        cell_width = width // grid_size[1]
        
        # Slice the image into grid cells
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                start_y = i * cell_height
                end_y = (i + 1) * cell_height
                start_x = j * cell_width
                end_x = (j + 1) * cell_width
                sliced_img = image[start_y:end_y, start_x:end_x]
                
                # Save the sliced image
                slice_name = os.path.splitext(image_file)[0] + f"_slice_{i}_{j}.jpg"
                cv2.imwrite(os.path.join(folder_path,"/sliced/", slice_name), sliced_img)

# Example usage
folder_path = "/images_path"  # Path to the folder containing images
grid_size = (20, 30)  # Define the grid size (rows, columns)

slice_and_save_images(folder_path, grid_size)

