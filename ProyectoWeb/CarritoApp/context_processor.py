def importe_total_carrito(request):
    
    total = 0

    if 'carrito' in request.session:
        for key, value in request.session['carrito'].items():
            total = float(total) + (float(float(value["precio"]) * float(value["cantidad"])))

    return {"importe_total_carrito": total}