import pdf2image

if __name__ == '__main__':
    # Convert PDF to list of images
    images = pdf2image.convert_from_path('/tmp/20240903-长桥证券-开户证明.pdf', dpi=300)

    # Save images as JPG
    for i, image in enumerate(images):
        image.save(f'/tmp/output_{i + 1}.jpg', 'JPEG')
