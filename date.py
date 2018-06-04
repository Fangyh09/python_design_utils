from datetime import datetime

now = datetime.now()
logdir = now.strftime("%Y%m%d-%H%M%S") + "/"
epoch_writer = SummaryWriter("../tf-writer/epoch/epoch-" + logdir)
batch_writer = SummaryWriter("../tf-writer/batch/batch-" + logdir)
