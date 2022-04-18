###########################################################################################
# leetcode problem https://leetcode.com/problems/flood-fill/
###########################################################################################
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    old_color = image[sr][sc]
    if old_color == newColor:
        return image

    image[sr][sc] = newColor
    pixel_stack = [(sr, sc)]
    while len(pixel_stack) > 0:
        pixel_x, pixel_y = pixel_stack.pop(-1)
        new_pixels = [(pixel_x - 1, pixel_y), (pixel_x + 1, pixel_y), (pixel_x, pixel_y + 1), (pixel_x, pixel_y - 1)]
        for i, (new_pixel_x, new_pixel_y) in enumerate(new_pixels):
            if (0 <= new_pixel_x <= len(image) - 1) and (
                    0 <= new_pixel_y <= len(image[0]) - 1):  # pixel lies within the image
                if image[new_pixel_x][new_pixel_y] == old_color:
                    image[new_pixel_x][new_pixel_y] = newColor
                    pixel_stack.append((new_pixel_x, new_pixel_y))

    return image