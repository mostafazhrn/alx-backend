import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const app = express();
const get_cli = promisify(client.get).bind(client);
const set_cli = promisify(client.set).bind(client);
const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]


const getItemById = (id) => {
    for (const item of listProducts) {
        if (item.Id === id) return item;
    }
}

const reserveStockById = async (itemId, stock) => {
    const item = getItemById(itemId);
    if (!item) return;
    if (item.stock < stock) throw new Error('Not enough stock available');
    await set_cli(itemId, stock);
}

const getCurrentReservedStockById = async (itemId) => {
    const stock = await get_cli(itemId);
    return stock;
}

app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)));
app.get('/list_products/:itemId', async (req, res) => {
    const id_num = Number(req.params.itemId);
    const item = getItemById(id_num);
    const currentReservedStock = await getCurrentReservedStockById(id_num);
    if (item) {
        item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
        res.json(item);
        return;
    }
    res.status(404).json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const id_num = Number(req.params.itemId);
    const item = getItemById(id_num);
    if (!item) {
        res.status(404).json({ status: 'Product not found' });
        return;
    }
    const currentReservedStock = await getCurrentReservedStockById(id_num);
    item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
    if ((item.stock - item.reservedStock) <= 0) {
        res.status(403).json({ status: 'Not enough stock available' });
        return;
    }
    reserveStockById(id_num, Number(currentReservedStock) + 1);
    res.json({ status: 'Reservation confirmed', id: id_num });
});
app.listen(1245);

