    widths, heights = zip(*(img.size for img in selected_images))

        total_width = sum(widths)
        max_height = max(heights)

        captcha_image = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for img in selected_images:
            captcha_image.paste(img, (x_offset, 0))
            x_offset += img.width
            return captcha_image, captcha_text
