CREATE TABLE DimProveedor (
    ProveedorID INT PRIMARY KEY IDENTITY,
    CodProveedor VARCHAR(255),
    NombreProveedor VARCHAR(255),
    DireccionProveedor VARCHAR(255),
    NumeroProveedor VARCHAR(255),
    WebProveedor VARCHAR(255)
);

CREATE TABLE DimProducto (
    ProductoID INT PRIMARY KEY IDENTITY,
    CodProducto VARCHAR(255),
    NombreProducto VARCHAR(255),
    MarcaProducto VARCHAR(255),
    Categoria VARCHAR(255)
);

CREATE TABLE DimSucursal (
    SucursalID INT PRIMARY KEY IDENTITY,
    CodSucursal VARCHAR(255),
    NombreSucursal VARCHAR(255),
    DireccionSucursal VARCHAR(255),
    Region VARCHAR(255),
    Departamento VARCHAR(255)
);

CREATE TABLE DimCliente (
    ClienteID INT PRIMARY KEY IDENTITY,
    CodigoCliente VARCHAR(255),
    NombreCliente VARCHAR(255),
    TipoCliente VARCHAR(255),
    DireccionCliente VARCHAR(255),
    NumeroCliente VARCHAR(255)
);

CREATE TABLE DimVendedor (
    VendedorID INT PRIMARY KEY IDENTITY,
    CodVendedor VARCHAR(255),
    NombreVendedor VARCHAR(255),
    Vacacionista VARCHAR(255)
);

CREATE TABLE DimTiempo (
    TiempoID INT PRIMARY KEY IDENTITY,
    Fecha DATE,
    Anio INT,
    Mes INT,
    Dia INT
);

CREATE TABLE HechosCompras (
    CompraID INT PRIMARY KEY IDENTITY,
    ProveedorID INT,
    ProductoID INT,
    SucursalID INT,
    TiempoID INT,
    Unidades INT,
    CostoU DECIMAL(18, 2),
    FOREIGN KEY (ProveedorID) REFERENCES DimProveedor(ProveedorID),
    FOREIGN KEY (ProductoID) REFERENCES DimProducto(ProductoID),
    FOREIGN KEY (SucursalID) REFERENCES DimSucursal(SucursalID),
    FOREIGN KEY (TiempoID) REFERENCES DimTiempo(TiempoID)
);

CREATE TABLE HechosVentas (
    VentaID INT PRIMARY KEY IDENTITY,
    ClienteID INT,
    ProductoID INT,
    SucursalID INT,
    VendedorID INT,
    TiempoID INT,
    Unidades INT,
    PrecioUnitario DECIMAL(18, 2),
    FOREIGN KEY (ClienteID) REFERENCES DimCliente(ClienteID),
    FOREIGN KEY (ProductoID) REFERENCES DimProducto(ProductoID),
    FOREIGN KEY (SucursalID) REFERENCES DimSucursal(SucursalID),
    FOREIGN KEY (VendedorID) REFERENCES DimVendedor(VendedorID),
    FOREIGN KEY (TiempoID) REFERENCES DimTiempo(TiempoID)
);

