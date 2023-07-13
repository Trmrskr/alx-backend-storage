-- Buy buy buy

CREATE TRIGGER `order_AIN`
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
