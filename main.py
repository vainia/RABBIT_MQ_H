from pathlib import Path

if __name__ == '__main__':

    names=['./RABBIT_MQ_'+n for n in ['H','E','L','W']]
    for n in names:
        if Path(n).exists():
            #subprocess.call([sys.executable, n+'/producer.py', '-m \'Hello, World!\'', '-r 3'])
            exec(open(n+'/producer.py').read())
            exec(open(n+'/consumer.py').read())
