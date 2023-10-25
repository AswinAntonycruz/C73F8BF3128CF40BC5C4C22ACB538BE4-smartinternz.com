def linearSearchProduct(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)

  return indices
  
products = ["shoes","boots","slipper","shoes", "loafer","shoes"]

target = "shose"
result= linearSearchProduct(products,target)
print(result)
 