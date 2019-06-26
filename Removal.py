import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def get_car_count(image_name):
    car_cascade = cv2.CascadeClassifier('cars.xml')
    img = cv2.imread(image_name, 1) #reading the image .
    width, height = img.shape[:2]
    if (height * width > 40000):
        dim=(800,800)
        img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Detect cars
    cars = car_cascade.detectMultiScale(gray,1.1, 1)
    idx=0
    count = 0
    # Draw border
    for (x, y, w, h) in cars:
        
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
        if w>100 and h>100:
            count += 1
            idx+=1
            new_img=img[y:y+int(3*h/4),x:x+w]
            #width=int(new_img.shape[1]*scale_percent/100)
            #height=int(new_img.shape[0]*scale_percent/100)
            #dim=(width,height)
            #resized = cv2.resize(new_img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(str(idx) + '.png', new_img)
    # Show image
    plt.figure(figsize=(10,20))
    plt.imshow(img)
    cv2.imwrite('im.jpg',img)
    return count

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    r = 0
    g = 0
    b = 0
    count = 0
    for (percent, color) in zip(hist, centroids):
        # print(percent)
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX
        elem=color.astype("uint8").tolist()


        grey = 0
        if((100 <= elem[0] <=200 and 100 <= elem[1] <= 200 and 100 <= elem[2] <= 200)):
            if (max(elem[0],elem[1]) - min(elem[0],elem[1]) < 18):
               if (max(elem[2],elem[1]) - min(elem[2],elem[1]) < 18): 
                   if (max(elem[0],elem[2]) - min(elem[0],elem[2]) < 18):
                       grey = 1
        # print(elem)
        if (percent > 0.50 and not(grey)):
            # elem_string = str(elem)
            # f.write(elem_string)
            elem_r = str(elem[0])
            elem_g = str(elem[1])
            elem_b = str(elem[2])
            f.write(elem_r)
            f.write(",")
            f.write(elem_g)
            f.write(",")
            f.write(elem_b)
            f.write("\n")
            print(elem)
            # print("case of dominant and not grey")
            return bar
        if (percent > 0.70 and grey):
            # f.write("[149, 159, 170]")
            f.write("149,159,170")
            f.write("\n")
            print([149, 159, 170])
            # print("case of dominant and grey")
            return bar
        else:
                    count += 1
                    r += elem[0]
                    g += elem[1]
                    b += elem[2]
    if (count != 0):
        li = [r/count,b/count,g/count]
        elem_r = str(li[0])
        elem_g = str(li[1])
        elem_b = str(li[2])
        f.write(elem_r)
        f.write(",")
        f.write(elem_g)
        f.write(",")
        f.write(elem_b)
        f.write("\n")
        # print([r/count,b/count,g/count])
        # print("case of average of the colours")
    else:
        f.write("149,159,170")
        f.write("\n")
        print([149, 159, 170])
    # return the bar chart
    return bar

# img = cv2.imread("5.png")


if __name__ == "__main__":
    try:
        for j in range(1000,1561):
            string1 = "nyc_trip_"
            string1 += str(j+1)
            string1 += ".jpg"
        # print(string1,"     ",type(string1))
            count1 = get_car_count(string1)
            f=open("colours.txt", "a+")
            print(count1)    
            for i in range(count1):
                string = ""
                string += str(i+1)
                string += ".png"
                # print(string,"                ",type(string))
                img = cv2.imread(string)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
                clt = KMeans(n_clusters=3) #cluster number
                clt.fit(img)

                hist = find_histogram(clt)
                bar = plot_colors2(hist, clt.cluster_centers_)
                # plt.axis("off")
                # plt.imshow(bar)
                # plt.show()
    except Exception:
        pass

